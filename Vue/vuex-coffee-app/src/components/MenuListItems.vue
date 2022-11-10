<template>
  <div id="box">
    <div 
      id="menu" 
      v-for="(menu, idx) in menuList" 
      :key="idx"
      @click="selectdedMenu(idx)"
      :class="{'is_selected' : menu.selected}"
      >
      <div id="imgBox">
        <img :src="menu.image" alt="아메리카노" id="thumbnail">
      </div>
      <span> {{menu.title}} </span>
      <span> {{menu.price}}원 </span>
    </div>
  </div>
</template>

<script>
export default {
  name:'MenuListItems',
  props:{
    menuList: Array,
  },
  methods:{
    selectdedMenu(idx){
      console.log(idx)
      this.$store.dispatch('updateSelectedMenu', idx)
    }
  }
}
</script>

<style>
  #imgBox{
    width:50px;
    height: 50px;
    border-radius: 10px;
    overflow: hidden;
    

  }
  #thumbnail{
    width: 100%;
    height: 100%;
    object-fit: cover;
    margin: 0;
  }
  #menu{
    border: groove 2px rgba(25, 138, 95, 0.896);
    border-radius: 10px;
    margin-top: 30px;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    height: 85px;
    align-items: center;
    padding: 0px 10px 0px 10px;
    
    
  }
  #menu:hover{
    background-color: rgba(25, 138, 95, 0.896);
  }
</style>