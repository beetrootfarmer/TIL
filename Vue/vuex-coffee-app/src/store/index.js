import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selSize : null,
    selMenu : null,
    orderList:[],
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '버블',
        price: 700,
        count: 0,
      },
      {
        type: '두유로 변경',
        price: 0,
        count: 0,
      },
    ],
    menuList: [
      {
        title : '아메리카노',
        price : '2000',
        selected : false,
        image : 'https://source.unsplash.com/featured/?coffee',
      },
      {
        title : '아샷추',
        price : '3500',
        selected : false,
        image : `https://source.unsplash.com/featured/?icetea`,
      },
      {
        title : '바닐라라떼',
        price : '3000',
        selected : false,
        image : `https://source.unsplash.com/featured/?latte`,
      },
    ],
    sizeList: [
      {
        name : 'small',
        price : 500,
        selected : false,
      },
      {
        name : 'regular',
        price : 700,
        selected : false,
      },
      {
        name : 'venti',
        price : 900,
        selected : false,
      },
    ],
  },
  getters: {
    totalOrderCount(state){
      return state.orderList.length
    },

    totalOrderPrice(state){
      const sum = state.orderList.reduce(function (total, x){
        return total + Number(x.menu.price) +Number(x.size.price)
      }, 0)
      console.log(sum)
      const priceList = state.optionList.map(x => x.price)
      const optPriceSum =  priceList.reduce((a, b) => a+ b, 0)
      return sum + optPriceSum
    },
  },
  mutations: {
    UPDATE_SELECTED_SIZE(state, idx){
      if (state.selSize != null){
        const already1 = state.selSize
        state.sizeList[already1].selected = false
      }
      state.selSize = idx
      state.sizeList[idx].selected = !state.sizeList[idx].selected
    },
    UPDATE_SELECTED_MENU(state, idx){
      if (state.selMenu != null){
        const already2 = state.selMenu
        state.menuList[already2].selected = false
      }
      state.selMenu = idx
      state.menuList[idx].selected = !state.menuList[idx].selected
    },
    ADD_ORDER: function (state) {
      const newOrder = {
        menu : state.menuList[state.selMenu],
        size : state.sizeList[state.selSize],
        option : state.optionList.map(x => x),
      }
      state.orderList.push(newOrder)
      alert('장바구니에 주문이 담겼습니다')

      const resetMenu = state.menuList.map(o => {
        return { title : o.title, price : o.price, selected : false , image: o.image}
      })
      state.menuList = resetMenu

      const resetOption = state.optionList.map(o => {
        return { type : o.type, price : o.price, count: 0}
      })
      state.optionList = resetOption

      const resetSize = state.sizeList.map(o => {
        return { name : o.name, price : o.price, selected : false}
      })
      state.sizeList = resetSize
      console.log(state.orderList)
    },
    UPDATE_OPTIONS_LIST(state,newOption){
      const idx = newOption.idx
      console.log(idx)
      if (newOption.count <= 0){
        state.optionList[idx].count = 0
      } else{
        state.optionList[idx].count = newOption.count
      }
    }

  },
  actions: {
    updateSelectedSize(context, idx){
      context.commit('UPDATE_SELECTED_SIZE', idx)
    },
    updateSelectedMenu(context, idx){
      context.commit('UPDATE_SELECTED_MENU', idx)
    },
    addOrder(context){
      // 선택한 메뉴가 없을 떄 alert
      if (context.state.selMenu == null){
        alert('음료를 선택해주세요!')
      }
      else if (context.state.selSize == null){
        alert('사이즈를 선택해주세요!')
      }
      else {
        context.commit('ADD_ORDER')
      }
    },
  },
  modules: {
  }
})