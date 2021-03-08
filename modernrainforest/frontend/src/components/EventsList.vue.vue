<style lang="scss" scoped>
  .events {
    margin-top: 10px;
    text-align: center;
    }
</style>

<template>


 <v-row  justify="center" align="center" >    

  <div class="events container">
    <h2 class="subtitle is-3">
    Check out our upcoming events
    </h2>

    <div class="columns is-multiline">
      <div v-for="product in products" :product="product" :key="product.id" class="column is-one-quarter">
        <router-link :to="'/event/' + product.id">
          <EventCard :product="product" />
        </router-link>
      </div>
    </div>
  </div>
</v-row> 

</template>


// <EventCard />

<script lang="ts">
import EventCard from './EventCard';
import { Vue, Component } from 'vue-property-decorator';
import { commitSetProductDetail } from '@/store/main/mutations';

@Component({
  components: {
    EventCard,
  },
})
export default class EventList extends Vue {

  public product: object =  {};
  public products: object[] = [
        {
          id: 1,
          name: 'Charity Ball',
          category: 'Fundraising',
          description: 'Spend an elegant night of dinner and dancing with us as we raise money for our new rescue farm.',
          featuredImage: 'https://placekitten.com/500/500',
          images: [
            'https://placekitten.com/500/500',
            'https://placekitten.com/500/500',
            'https://placekitten.com/500/500',
          ],
          location: '1234 Fancy Ave',
          date: '12-25-2019',
          time: '11:30',
        },
        {
          id: 2,
          name: 'Rescue Center Goods Drive',
          category: 'Adoptions',
          description: 'Come to our donation drive to help us replenish our stock of pet food, toys, bedding, etc. We will have live bands, games, food trucks, and much more.',
          featuredImage: 'https://placekitten.com/500/500',
          images: [
            'https://placekitten.com/500/500',
          ],
          location: '1234 Dog Alley',
          date: '11-21-2019',
          time: '12:00',
        },
  ];

}

</script>

