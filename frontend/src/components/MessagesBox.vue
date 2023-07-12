<script setup lang="ts">
    import {ref} from 'vue'
    import type { Message } from '@/interfaces/message';
    defineProps<{
        messages: Message[]
    }>()
    const lastSize = ref(400)
    const onChange = (source) => {
        if(source.verticalSize != lastSize.value){
            lastSize.value = source.verticalSize
            source.ref.setScrollPercentage('vertical', 1, 150)
        }
    }
</script>
<template>
    <q-scroll-area @scroll="onChange" style="height: 400px; min-height: 400px;">
        <div class="q-pa-lg">
            <div v-for="m in messages" :key="m.content">
                <q-chat-message :sent="m.sender != 'bot'" :text="[m.content]"/>
            </div>
        </div>
    </q-scroll-area>

</template>

<style scoped>
</style>