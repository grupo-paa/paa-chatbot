<script setup lang="ts">
    import type { Message } from '@/interfaces/message';
    defineProps<{
        message: Message
        sent: boolean
    }>()
</script>
<template>
    <div v-if="sent" class="text-right">{{ message.content }}</div>
    <div v-else >{{ message.content }}</div>
</template>