<template>


    <v-app-bar
      absolute
      color="#43a047"
      dark
      shrink-on-scroll
      dense
      src="https://i.picsum.photos/id/482/2560/1440.jpg?hmac=FB15e_vNXF-H_-ASr324yxYQVlvkycm26rRTXVGK4R0"
    >

            <v-app-bar-title to="/">Modern Rainforest</v-app-bar-title>

            <v-spacer></v-spacer>



    <v-row justify="center" align="center">
        <v-col cols="3" sm="8" md="4">
        <v-btn icon>
        <router-link to="/" class="navbar-item">Home</router-link>
        </v-btn>
        </v-col>

        <v-col cols="3" sm="8" md="4">
        <v-btn icon>
        <router-link to="/about" class="navbar-item">About</router-link>
        </v-btn>
        </v-col>

        <v-col cols="3" sm="8" md="4">
        <v-btn icon>
                <strong><router-link to="/login" class="navbar-item">Sign in</router-link></strong>
        </v-btn>
        </v-col>

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