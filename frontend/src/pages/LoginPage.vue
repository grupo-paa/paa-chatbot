<template>
    <div class="row window-height window-width justify-center items-center">
        <q-form class="q-gutter-md" @submit="onSubmit" @reset="onReset">
            <q-input 
                v-model="user" 
                placeholder="Usuario"
                lazy-rules
                :rules="[val => val && val.length > 0 || 'Por favor digite um usuário']"
            />
            <q-input 
                v-model="password" 
                placeholder="Senha"
                type="password"
                lazy-rules
                :rules="[val => val && val.length > 0 || 'Por favor digite uma senha']"
            />
            <q-btn type="submit" label="logar" color="secondary"/>
        </q-form>
    </div>
</template>

<script setup lang="ts">
import {ref} from 'vue'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'
import {Cookies} from 'quasar'
import { useRouter } from 'vue-router'
const $q = useQuasar()

const user = ref('')
const password = ref('')
const router = useRouter()

const onSubmit = () => {
    const json = JSON.stringify({user: user.value, password: password.value})
    api.post('/auth/login', json, {
        headers: {
            // Overwrite Axios's automatically set Content-Type
            'Content-Type': 'application/json'
        }
    })
    .then((res) => {
        Cookies.set('user_info', JSON.stringify(res.data.data))
        router.push({
            path:'/'
        })
    })
    .catch(()=>{
        $q.notify({
            color: 'negative',
            position: 'top',
            message: 'Usuario ou senha invalidos',
            icon: 'report_problem'
        })
    })
}
const onReset = () => {
    user.value = null
    password.value = null
}

</script>

<style scoped>

</style>
