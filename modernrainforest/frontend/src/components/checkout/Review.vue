<template>
    <v-stepper-content step="3">
        <v-list disabled dense>
            <v-subheader class="title">
            Review Order 
            </v-subheader>
            <v-list-item-group color="primary">
                <v-list-item
                v-for="(value,name) in data"
                :key="name">
                    <v-list-item-content>
                        <v-list-item-title>
                          {{ name }}: {{ value }}
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
        </v-list>
        <v-btn color="primary"  @click="submitOrder" to="/thankyou">
        SUBMIT
        </v-btn>

        <v-btn text @click="previous">
        Go Back
        </v-btn>
    </v-stepper-content>
</template>



<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class Review extends Vue {
  @Prop() public previous !: () => void;
  @Prop() public submitOrder !: () => void;
  @Prop(Object) public data: object = [];

}

</script>


