
<style lang="scss" scoped>

.hero {  
    margin-top: 165px;
    background-repeat: no-repeat;
    height: 720px;
    width: 100%;
    }
  .title{
    font-size: 13.2rem;
    margin-bottom:10px;
  }
  .is-button {
    font-size: 1.2rem;
    color:white;
    width:300px;
  }

</style>

<template>
  <v-container class="home" >
    <section justify="center" align="center">
      <v-parallax class="hero" height="720" src="https://i.picsum.photos/id/1063/2560/1440.jpg?hmac=wov80KgofTtCwHrl6JLolFq0EunCYEMKI5zmc2VLCvc">

        <div class="text-xs-center">
                <h1 class="title">
                  Welcome to the Modern Rainforest       
                </h1>
                
                <v-btn to="/event/1" color="rgb(34,34, 34, 0.8)" class="is-button">Browse Newreleases</v-btn>
        </div>
        
      </v-parallax>

       
      </section>
      <EventsList />
  </v-container>
</template>




<script>

import EventsList from '@/components/EventsList.vue';
import { Component, Vue } from 'vue-property-decorator';

@Component({
  components: {
    EventsList,
  },
})

export default class Home extends Vue {

}
</script>

