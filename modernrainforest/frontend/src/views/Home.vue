<template>

  <v-container class="home" >
    <section class="hero is-dark">
      <v-parallax height="720" src="https://i.picsum.photos/id/1063/2560/1440.jpg?hmac=wov80KgofTtCwHrl6JLolFq0EunCYEMKI5zmc2VLCvc">


        <h1 class="title">
          Welcome to the Modern Rainforest       
        </h1>
        <h2 class="subtitle">
          Make sure you check out our upcoming events below
        </h2>
        
        <v-btn color='#2c3e50' class="button is-xl is-dark">Browse Events</v-btn>


      </v-parallax>
      </section>

      <h2 class="subtitle is-3"> Check out our upcoming EventsList</h2>
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
<style lang="scss" scoped>
  .hero {   
    margin-top: 0px;
    text-align: center;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 720px;
  }


  .is-xl {
    font-size: 1.7rem;
  }
</style>
