<template>
    <q-form @submit="sendMessage" ref="msgForm" class="row justify-center q-gutter-x-sm">
        <q-input hide-bottom-space rounded outlined lazy-rules :rules="[(text) => text && text.length > 0 || 'Por favor, digite uma mensagem']" class="col-9" v-model="text"></q-input>
        <q-btn rounded flat color="secondary" class="col-1" type="submit" icon="send"/>
    </q-form>
</template>

<script setup lang="ts">
    import { ref } from 'vue';

    const emit = defineEmits<{
        sendMessage: [text: string]
    }>()

    const msgForm = ref(null)

    const sendMessage = () => {
        emit('sendMessage', text.value) 
        text.value = ''
        msgForm.value.reset()
    }
    const text = ref('')
</script>

<style scoped>
</style>