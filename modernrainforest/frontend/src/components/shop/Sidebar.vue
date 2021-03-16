<template>
    <div>
        <v-sheet v-if="$vuetify.breakpoint.mdAndUp"
                :elevation="4"
                class="pa-8"
                >
        <h3>Filters</h3>
        </v-sheet>

        <v-expansion-panels v-else>
            <v-expansion-panel>
                <v-expansion-panel-header expand-icon = "fa-angle-down">
                    Filters
                </v-expansion-panel-header>
                 <v-expansion-panel-content>
                    <v-radio-group v-model="priceFilter" :mandatory="true">
                        <v-radio v-for="(price, i) in prices"
                        :key="i"
                        :label="price"
                        :value="i">
                        </v-radio>
                    </v-radio-group>
                 </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
    </div>
</template>


<script lang="ts">

import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Sidebar extends Vue {
    public prices: object = [
        'Any',
        'Under $25',
        '$25 to $100',
        '$100 to $500',
        'Over $500',
    ];
    public priceFilter: number = 0;
    public checkbox: boolean = true;
}
</script>