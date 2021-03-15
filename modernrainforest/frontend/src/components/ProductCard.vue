<template>
  <v-card :loading="loading"  class="mx-auto my-12" max-width="374" >
    <template slot="progress">
      <v-progress-linear color="deep-purple" height="10" indeterminate  ></v-progress-linear>
    </template>

    <v-img height="250" src="https://cdn.vuetifyjs.com/images/cards/cooking.png" ></v-img>

    <v-card-title>{{product.asin}}, {{product.brand}}</v-card-title>

    <v-card-text>
      <v-row align="center" class="mx-0"  >
        <v-rating  :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14" ></v-rating>

        <div class="grey--text ml-4">
          {{product.rating}}
        </div>
      </v-row>

      <div class="my-4 subtitle-1">
        {{product.price}}
      </div>

      <div>{{product.dimensions}}</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Tonight's availability</v-card-title>

    <v-card-text>
      <v-chip-group v-model="selection" active-class="deep-purple accent-4 white--text"  column >
        <v-chip>{{product.date}}</v-chip>

        <v-chip>7:30PM</v-chip>

        <v-chip>8:00PM</v-chip>

        <v-chip>9:00PM</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn color="deep-purple lighten-2" text @click="reserve" >
        Add to Shopping Cart
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class ProductCard extends Vue {
  @Prop(Object) public product: object | null;
  public loading: boolean = false;
  public selection: number = 1;
  public reserve() {
      this.loading = true;
      setTimeout(() => (this.loading = false), 2000);
    }
}

</script>