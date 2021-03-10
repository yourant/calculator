<template>
  <v-app-bar absolute color="white" elevate-on-scroll scroll-target="#scrolling-techniques-7">
    <v-row>


      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-app-bar-title to="/">Modern Rainforest</v-app-bar-title>
  

      <v-spacer></v-spacer>

      <v-card elevation="1">
                <v-text-field
                hide-details
                prepend-icon="mdi-magnify"
                single-line></v-text-field>
      </v-card>


    

    <v-divider
      class="mx-4"
      vertical
    ></v-divider>
          <v-btn icon>
          <router-link to="/">Home</router-link>
          </v-btn>

    <v-divider
      class="mx-4"
      vertical
    ></v-divider>


          <v-btn icon>
          <router-link to="/about" >About</router-link>
          </v-btn>

    <v-divider
      class="mx-4"
      vertical
    ></v-divider>

          <v-btn icon>
                  <strong><router-link to="/login" >Sign in</router-link></strong>
          </v-btn>


    </v-row>
  </v-app-bar>

</template>
<script>
export default {
    name: 'Nav'
}
</script>

<style lang="scss" scoped>


</style>