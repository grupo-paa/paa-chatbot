<template>
    <div class="row justify-center q-gutter-x-sm">
        <q-input rounded standout class="col-9" v-model="text"></q-input>
        <q-btn rounded color="secondary" class="col-1" @click="emit('sendMessage', text)" icon="send"/>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';

    const emit = defineEmits<{
        sendMessage: [text: string]
    }>()
    const text = ref('')
</script>

<style scoped>
</style>