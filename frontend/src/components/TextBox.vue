<template>
    <q-form @submit="sendMessage" class="row justify-center q-gutter-x-sm">
        <q-input rounded standout class="col-9" v-model="text"></q-input>
        <q-btn rounded flat color="secondary" class="col-1" type="submit" icon="send"/>
    </q-form>
</template>

<script setup lang="ts">
    import { ref } from 'vue';

    const emit = defineEmits<{
        sendMessage: [text: string]
    }>()
    const sendMessage = () => {
        emit('sendMessage', text.value) 
        text.value = ''
    }
    const text = ref('')
</script>

<style scoped>
</style>