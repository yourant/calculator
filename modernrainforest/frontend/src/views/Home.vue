
<style lang="scss" scoped>
  .hero {  
    margin-top: 165px;
    text-align: center;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 720px;
    }
  .is-button {
    font-size: 1.7rem;
    margin-left:710px;
    width:300px;
  }
  .title{
    font-size: x-large;
    margin-bottom:10px;
  }

</style>

<template>

  <v-container class="home" >
    <section class="hero is-dark">
      <v-parallax height="720" src="https://i.picsum.photos/id/1063/2560/1440.jpg?hmac=wov80KgofTtCwHrl6JLolFq0EunCYEMKI5zmc2VLCvc">


        <h1 class="title">
          Welcome to the Modern Rainforest       
        </h1>
        

        <v-btn color='white' class="is-button">Browse Events</v-btn>

      </v-parallax>
      </section>

      <h2 class="subtitle"> Check out our upcoming EventsList</h2>
      <EventsList />
  </v-container>
</template>




<script>

import EventsList from '@/components/EventsList.vue';

export default {
  name: 'home',
  components: {
    EventsList,
  },
};
</script>

