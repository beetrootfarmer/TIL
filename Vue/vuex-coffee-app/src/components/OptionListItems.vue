<template>
  <div>
    <div id="size">
      <span> {{selectedOption.type}} </span>
      <span> {{selectedOption.price}}원 </span>
      <button @click="deleteOption()">-</button>
       {{selectedOption.count}}
      <button @click="addOption()">+</button>
    </div>
  </div>
</template>

<script>
export default {
    name:'OptionListItems',
    props:{
        selectedOption : Object,
        idx : Number,
    },
    methods:{
        addOption(){
            const newOp = {
                type: this.selectedOption.type,
                count : this.selectedOption.count+1,
                idx : this.idx,
            }
            this.$store.commit('UPDATE_OPTIONS_LIST', newOp)
        },
        deleteOption(){
            const newOp = {
                type: this.selectedOption.type,
                count : this.selectedOption.count-1,
                idx : this.idx,
            }
            this.$store.commit('UPDATE_OPTIONS_LIST', newOp)
        }
    }

}
</script>

<style>

</style>