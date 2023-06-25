<template>
    <div class="bg-slate-500 flex">
        <textarea v-model="text"></textarea>
        <button @click="emit('sendMessage', text)">Enviar</button>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';

    const emit = defineEmits<{
        sendMessage: [text: string]
    }>()
    const text = ref("")
</script>

<style scoped>
    textarea { 
        border-radius: 30px 0px 0px 30px;
        border: none;
        background-color: rgb(169, 168, 224);
        max-width: 800px;
        min-width: 100px;
        width: 100%;
        height: fit-content;
        margin: 10px 0px 10px 10px;
        resize: none;
    }
    button {
        height: fit-content;
        background-color: rgb(49, 47, 194);
        color: white;
        border: none;
        border-radius: 0px 30px 30px 0px;
        height: 34px;
        margin: 10px 10px 10px 0px;
    }
    button:hover {
        cursor: pointer;
    }
</style>