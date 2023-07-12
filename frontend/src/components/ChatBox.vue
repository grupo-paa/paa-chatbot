<template>
    <div class="column justify-between">
        <div class="bg-positive border-up">
            <Messages :messages="messages"/>
        </div>
        <div class="border-down col-4 bg-grey-2 q-py-sm textbox">
          <Textbox @send-message="(text)=>{sendMessage(text)}"/>
        </div>
    </div>
</template>
<script setup lang="ts">
    import Messages from '../components/MessagesBox.vue'
    import Textbox from '../components/TextBox.vue'
    import type {Message} from '../interfaces/message'
    import { onMounted, ref } from 'vue';
    import type {Ref} from 'vue'
    import axios from 'axios';

    const messages: Ref<Message[]> = ref([])

    const emit = defineEmits(['jar'])

    const sendMessage = async (text: string)=>{
        messages.value = [...messages.value, {sender: 'user', content: text}] 
        try {
        let res = await axios({
            method:'post',
            url: 'http://localhost:5000/chat',
            data: {message:text}
        });
        let receivedMessage: Message = res.data
        messages.value = [...messages.value, receivedMessage]
        const s = receivedMessage.content.toLowerCase()
        if(s.includes("jar jar")){
            emit('jar')
        }
        } catch (e){
        axios.isAxiosError(e) ? console.log('axios:', e) : console.log(e);
        }
    }
    onMounted(async () => {
        // await sendMessage("teste2")
    })
</script>

<style scoped lang="scss">
.border-up{
    border-radius: 6px 6px 0 0;
}
.border-down{
    border-radius: 0 0 6px 6px;
}
</style>