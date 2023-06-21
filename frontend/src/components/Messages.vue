<script setup lang="ts">
    import type { Message } from '@/interfaces/message';
    defineProps<{
        messages: Message[]
    }>()

</script>
<template>
    <h1> teste </h1>
    <div v-for="m in messages">{{m.content}}</div>
</template>