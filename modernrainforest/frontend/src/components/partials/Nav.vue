<template>
<nav>

<v-app-bar flat absolute color="white" elevate-on-scroll scroll-target="#scrolling-techniques-7">
  <v-app-bar-title class = 'text-uppercase grey--text' to="/">   
    <span class="font-weight-light">Modern Rainforest</span>
    <span>Race</span>
  </v-app-bar-title>


  <v-spacer></v-spacer>

  <v-card elevation="1">
      
            <v-text-field 

            hide-details
            single-line ></v-text-field>
            
  </v-card>

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
        <v-btn flat color="blue darken-2" to="/login">
                <span><strong>Sign in</strong></span>
                <v-icon> exit_to_app</v-icon>
        </v-btn>

</v-app-bar>

</nav>
</template>







<script>
export default {
    name: 'Nav',
};
</script>

<style lang="scss" scoped>


</style>