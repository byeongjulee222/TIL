import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
  }
})


// 상태
// 1. state : 데이터
// 2. getters : computed 동작 작성
// 3. mutations : methods 정의, state를 변경하기 위해서 반드시 동기적인 method만 사용 가능
// 첫번째 인자는 항상 state, 호출은 commit으로 !
// 4. actions : methods 정의, 비동기 처리가 가능한 method 또한 사용 가능
// actions가 mutations와 구분된 이유 :
//  다양한 컴포넌트에서 vuex를 통해 상태관리, 메서드 호출 등을 하게될텐데, 그 때 동기와 비동기를 구분하기 위해.
// 첫번째 인자는 항상 context(state/commit/dispatch 등), 호출은 dispatch로 된다.
