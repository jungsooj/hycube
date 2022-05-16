<template>
    <div class="component">
        <ComponentMenu v-for="(d, index) in data" :listName="d" :key="index"></ComponentMenu>
    </div>
</template>

<script>
'use strict';
let jsonData = require('../data/AitData.json');

import ComponentMenu from './ComponentMenu.vue'

export default{
 components: {
    ComponentMenu
  },
  data: () => {
      return {
           data: Object.keys(jsonData),
        }
    }
}
</script>