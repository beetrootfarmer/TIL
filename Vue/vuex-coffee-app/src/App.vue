<template>
  <div id="app">
    <h1 id='title'>Coffee Order App</h1>
    <div id="selectBoxMain">
      <MenuList id="selectItem"/>
      <SizeList id="selectItem"/>
      <OptionList id="selectItem"/>
    </div>
    <button 
      id="cartBtn"
      @click="addOrder"
      >장바구니 담기</button>
      <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
import OptionList from '@/components/OptionList'

export default {
  name: 'App',
  components:{
    MenuList,
    SizeList,
    OrderList,
    OptionList
  },
  methods:{
    addOrder(){
      this.$store.dispatch("addOrder")
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}
#selectBoxMain{
  width: 100%;
  background-color: rgba(194, 194, 194, 0.241);
  display: flex;
  justify-content:space-evenly;
  border-radius: 10px;
  }
#app{
  text-align: center;
  margin: 1%;
}
#title{
  margin: 10px;
  margin-top: 30px;
}
#selectItem{
  width: 48%;
  margin-top: 2%;
  margin-bottom: 2%;
}
ul {
  list-style: none;
}
#cartBtn{
  border: none;
  margin-top: 15px;
  width: 100%;
  display: block;
  height: 50px;
  border-radius: 10px;
  background-color: rgba(25, 138, 95, 0.896);
  color : white;
  font-size: 1.3em;
  font-weight: bold;
}
#cartBtn:hover{
  background-color: rgba(71, 122, 102, 0.896);

  border: solid 2px rgba(25, 138, 95, 0.896);
}
</style>
