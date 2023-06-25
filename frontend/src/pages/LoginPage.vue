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
                lazy-rules
                :rules="[val => val && val.length > 0 || 'Por favor digite uma senha']"
            />
            <q-btn type="submit" label="logar" color="secondary"/>
        </q-form>
    </div>
</template>

<script setup lang="ts">
import {ref} from 'vue'
const user = ref()
const password = ref()
const onSubmit = () => {
    console.log(user.value, password.value)
}
const onReset = () => {
    user.value = null
    password.value = null
}

</script>

<style scoped>

</style>
