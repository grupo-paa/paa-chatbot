<script setup lang="ts">
    import type { Message } from '@/interfaces/message';
    defineProps<{
        messages: Message[]
    }>()
</script>
<template>
    <div class="q-pa-lg">
        <div v-for="m in messages" :key="m.content">
            <q-chat-message :sent="m.sender != 'bot'" :text="[m.content]"/>
        </div>
    </div>
</template>

<style scoped>
</style>