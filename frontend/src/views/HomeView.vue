<template>
  <main>
    <Messages :messages="messages"/>
    <h2 class="text-3xl underline">teste 34</h2>
    <Textbox @send-message="(text)=>{sendMessage(text)}"/>
  </main>
</template>

<script setup lang="ts">

  import Messages from '../components/Messages.vue'
  import Textbox from '../components/Textbox.vue'
  import type {Message} from '../interfaces/message'
  import { onDeactivated, onMounted, ref } from 'vue';
  import type {Ref} from 'vue'
  import axios from 'axios';

  const messages: Ref<Message[]> = ref([])

  const sendMessage = async (text: string)=>{
    messages.value = [...messages.value, {sender: 'user', content: text}] 
    try {
      let res = await axios({
          method:"post",
          url: "http://localhost:5000/message",
          data: {message:text}
      });
      let receivedMessage: Message = res.data
      messages.value = [...messages.value, receivedMessage] 
    } catch (e){
      axios.isAxiosError(e) ? console.log('axios:', e) : console.log(e);
    }
  }
  onMounted(async () => {
    await sendMessage("teste2")
  })
</script>

<style></style>
