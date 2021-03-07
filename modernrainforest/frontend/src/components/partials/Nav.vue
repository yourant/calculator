<style lang="scss" scoped>

.font-weight-light {
  color: white;
  font-size: 1.7rem;
  }
.navIcon{
  border: 1px solid #ccc;
  background-color: white;
  color:white;
  padding: 10px;
}
.searchbar{
  background-color: white;
  width: 10px;
}
</style>



<template>
<nav>

<v-app-bar flat absolute color="black" elevate-on-scroll scroll-target="#scrolling-techniques-7">
  
  <v-app-bar-nav-icon class="navIcon" @click="drawer = !drawer"></v-app-bar-nav-icon>


    <v-app-bar-title >   
      <span class="font-weight-light">ModernRainforest</span>
    </v-app-bar-title>


  <v-spacer></v-spacer>



<v-text-field class="searchbar" hide-details single-line ></v-text-field><v-btn>Search<v-icon>mdi-magnify</v-icon></v-btn>

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

<v-navigation-drawer v-model="drawer" app class="white">
  <v-icon v-html="miniDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
  <v-list-tile-title  @click="drawer = false">Collapse</v-list-tile-title>
</v-navigation-drawer>

</nav>


</template>






<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';


@Component
export default class Nav extends Vue {
  public drawer: boolean= false;
}
</script>

