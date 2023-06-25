<template>
  <main>
<<<<<<< HEAD
    <Messages :messages="messages"/>
    <h2 class="text-3xl underline">teste 34</h2>
    <Textbox @send-message="(text)=>{sendMessage(text)}"/>
=======
    <div class="chatbox">
      <!-- <div class="b"> -->
        <section class="section-msgs bottom-msg">
          <Messages :messages="messages"/>
        </section>
        <section class="section-input bottom-box">
          <Textbox @send-message="(text)=>{sendMessage(text)}"/>
        </section>

      <!-- </div> -->
    </div>
>>>>>>> 11c551cbd29b7b14ae7731c5bf68c955e4833a58
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

<<<<<<< HEAD
<style></style>
=======
<style>
  .chatbox {
    margin: auto;
    /* margin-left: auto; */
    background-color: rgba(0,0,0,0.5);
    opacity: 65%;
    max-width: 800px;
    height: 500px;
    border-radius: 30px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    /* flex-direction: column; */
    position: relative;
  }
  
  .section-input, .section-msgs {
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    align-items: center;
    display: flex;
    justify-content: center;
    position: relative;

    /* flex-grow: 1; */
    /*  */
  }
  .bottom-box {
      position: absolute;
      bottom: 0;
      width: 100%;
  }

  .bottom-msg {
      position: absolute;
      bottom: 50px;
      right: 0;
      width: 100%;
  }

  /* .b {
    display: block;
    position: relative;
  } */

  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>
>>>>>>> 11c551cbd29b7b14ae7731c5bf68c955e4833a58
