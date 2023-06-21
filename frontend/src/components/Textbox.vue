<template>
    <textarea v-model="text"></textarea>
    <button @click="emit('sendMessage', text)">enviar</button>
</template>

<script setup lang="ts">
    import { ref } from 'vue';

    const emit = defineEmits<{
        sendMessage: [text: string]
    }>()
    const text = ref("")
</script>