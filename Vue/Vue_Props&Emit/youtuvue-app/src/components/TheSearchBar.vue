<template>
  <div class="search-box">
    <input 
      id="searchBar"
      v-model="keyword"
      @keyup.enter="getKeyword"
      type="text" class="search-txt"  placeholder="    검색">
  </div>
</template>

<script src="https://kit.fontawesome.com/5c53a7748a.js" crossorigin="anonymous"></script>
<script>
export default {
  name : 'TheSearchBar',
  data (){
    return{
      keyword:null,
    }
  },
  methods:{
    getKeyword(){
      // console.log(this.keyword)
      this.$emit('search-keyword', this.keyword)
      this.keyword = null
    }
  }
}
</script>

<style>

  .search-box{
  padding: 10px;
  position:inherit;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  height: 30px;
  background-color: #fff;
  border: 1px solid #1d9672;
  border-radius: 30px;
  transition: 0.4s;
  width:30px;
}
.search-box:hover{
  box-shadow: 0px 0px .5px 1px #1d9672;
  width: 282px;
  background-color: #fff;
}
.search-txt{
  display: flex;
  padding: 0;
  width: 0px;
  border:none;
  background: none;
  outline: none;
  float: left;
  font-size: 1rem;
  line-height: 30px;
  transition: .4s;
}
.search-box:hover > .search-txt{
  width: 240px;
  padding: 0 6px;
}
</style>