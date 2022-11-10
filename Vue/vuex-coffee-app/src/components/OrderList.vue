<template>
  <div class="orderListBox">
    <div class="orderListBoxTitle">
        <h2>주문내역</h2>
    </div>
        <div 
        id="selBox" 
        v-for="(select, idx) in ol" 
        :key="idx"
        >
            <div class="selLeft">
            <p>총 {{totalOrderCount}} : {{totalOrderPrice}}원</p>
                <div id="imgBox">
                    <img :src="select.menu.image" alt="아메리카노" id="thumbnail">
                </div>
                <span> {{select.menu.title}} </span>
                <span> {{select.size.name}} </span>
            </div>
            <div class="selRight">
                <span> 가격 : {{Number(select.size.price) + Number(select.menu.price)}}</span>
                <div v-for="(opt, idx) in select.option" :key="idx">
                    <span>{{opt.type}} {{opt.count}}</span> |
                </div>
            </div>
        </div>
        <hr>
    </div>
</template>

<script>
export default {
    name : 'OrderList',
    computed:{
        ol(){
            return this.$store.state.orderList
        },
        totalOrderCount(){
            return this.$store.getters.totalOrderCount
        },
        totalOrderPrice(){
            return this.$store.getters.totalOrderPrice
        },
        optionList(){
            return this.$store.state.optionList
        },
    }
}
</script>

<style>
    .orderListBox{
        background-color: rgba(236, 241, 245, 0.839);
        margin-top: 13px;
        margin-bottom: 30px;
        border-radius: 15px;
        justify-content: center;
        padding: 2%;
    }
    .orderListBoxTitle{
        margin: 3%;
        text-align: left;
        display: block;
        
    }
    .selLeft > *{
        margin: 7px;
    }
    .selLeft {
        text-align: left;
    }
    #selBox{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        margin: 3%;
    }
</style>