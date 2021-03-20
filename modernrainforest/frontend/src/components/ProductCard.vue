<template>
  <v-card :loading="loading"  class="mx-auto my-12" max-width="374" >
    <template slot="progress">
      <v-progress-linear color="deep-purple" height="10" indeterminate  ></v-progress-linear>
    </template>

    <v-img height="250" :src=product.imagelink ></v-img>

    <v-card-title>{{product.brand}}</v-card-title>
      <v-btn text @click="goAmazon()">
      {{product.asin}}
      </v-btn>
    <v-card-text>
      <v-row align="center" class="mx-0"  >
      <v-rating  :value=Number(product.rating)
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
       Price: ${{product.price}}
      </div>
      <div>Dimensiosn:{{product.dimensions}}</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Released Since:

    </v-card-title>

    <v-card-text>
       {{product.first_date || 'New Released'}}
    </v-card-text>

    <v-card-actions>
      <v-btn color="deep-purple lighten-2" text @click="addToCart" >
        Add to Shopping Cart
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class ProductCard extends Vue {
  @Prop(Object) public product!: object | null;
  public loading: boolean = false;
  public selection: number = 1;
  public addToCart() {
      this.loading = true;
      setTimeout(() => (this.loading = false), 2000);
    };
  public goAmazon() {
    window.open(`https://www.amazon.com/dp/${this.product.asin}`, '_blank')
  }
}

</script>