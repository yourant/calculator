<style lang="scss" scoped>

.font-weight-light {
  color: white;
  font-size: 1.7rem;
  }
.navIcon{
  size: 25;
  border: 2px solid #ccc;
  background-color: white;
}
.searchbar{
  border-radius:50px;
  background-color: white;
}
.navdrawer{

  margin-top: 85px;
}


</style>



<template>
<nav>

<v-app-bar flat absolute color="black" elevate-on-scroll scroll-target="#scrolling-techniques-7">


  <v-app-bar-nav-icon dense class="navIcon" @click="drawer = !drawer"></v-app-bar-nav-icon>


    <v-app-bar-title >   
      <span class="font-weight-light">ModernRainforest</span>
    </v-app-bar-title>
  <v-img 
    class="mx-2"
    src="https://st3.depositphotos.com/27847728/34695/v/1600/depositphotos_346956532-stock-illustration-initial-letter-logo-design-vector.jpg"
    max-height="40"
    max-width="40"
    contain
  ></v-img>
  
  <v-spacer></v-spacer>

    <v-toolbar  max-width="250" dense >
      <v-text-field label="Search for products" class="searchbar" prepend-icon="mdi-magnify" hide-details single-line ></v-text-field>
    </v-toolbar>

  
    <v-divider class="mx-4" vertical></v-divider>

        <v-btn to="/">
            <span>Home</span>
            <v-icon>home</v-icon>
        </v-btn>

    <v-divider class="mx-4" vertical></v-divider>
        <v-btn flat to="/about" >             
            <span> About</span>
            <v-icon>info</v-icon>
        </v-btn>

      <v-divider class="mx-4" vertical></v-divider>
        <v-btn flatdepressed to="/login">
                <span>Sign in</span>
                <v-icon> exit_to_app</v-icon>
        </v-btn>
</v-app-bar>


<v-navigation-drawer v-model="drawer" app class="navdrawer">
  <v-btn to="/">Back Home</v-btn>
  <v-icon v-html="miniDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
</v-navigation-drawer>


</nav>
</template>


<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';


@Component
export default class Nav extends Vue {
  public drawer: boolean = false;
}

</script>