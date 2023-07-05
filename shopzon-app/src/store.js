import {
  legacy_createStore as createStore,
  combineReducers,
  applyMiddleware,
} from 'redux'
import thunk from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'
import {
  productListReducer,
  productTopRatedReducer,
  productDetailsReducer,
  productCreateReviewReducer,
} from './reducers/productReducers'
import {userLoginReducer, userRegisterReducer} from './reducers/userReducers'

const reducer = combineReducers({
  productList: productListReducer,
  productTopRated: productTopRatedReducer,
  userLogin: userLoginReducer,
  userRegister: userRegisterReducer,
  productDetails: productDetailsReducer,
  productCreateReview: productCreateReviewReducer,
})

const userInfoFromStorage = localStorage.getItem('userInfo')
  ? JSON.parse(localStorage.getItem('userInfo'))
  : null

const initialState = {
  userLogin: {userInfo: userInfoFromStorage},
}

const middleware = [thunk]

const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
)

export default store
