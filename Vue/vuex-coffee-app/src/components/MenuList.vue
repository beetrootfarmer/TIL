<template>
  <div id="menuListItems">
    <div 
      class="selectBox" 
      >
      <h3>음료를 고르세요</h3>
      <MenuListItems 
        :menu-list="menuList"
        />
    </div>
  </div>
</template>

<script>
import MenuListItems from '@/components/MenuListItems'
export default {
  components: {
    MenuListItems,
  },
  computed:{
    menuList(){
      return this.$store.state.menuList
    }
  }
}
</script>

<style>
   #menuListItems{

   }
   .selectBox{
    background-color: white;
    /* margin-right: 5%;
    margin-top: 5%;
    margin-bottom: 5%; */
    border-radius: 10px;
    padding: 7%;
    width: 100%;
   }
</style>