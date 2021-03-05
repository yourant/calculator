<template>


 <v-row  justify="center" align="center" >    

    
        <v-col xs="12" sm="8" md="4">
        <EventCard />
        </v-col>

        <v-col xs="12" sm="8" md="4">
        <EventCard />
        </v-col>

        <v-col xs="12" sm="8" md="4">
        <EventCard />
        </v-col>



</v-row> 

</template>



<script>
  import EventCard from '@/components/EventCard';
  export default {
    name: 'EventsList',
    components : {
      EventCard
    }
  }
</script>
<style lang="scss" scoped>
  .events {
    margin-top: 10px;
    text-align: center;
  }
</style>