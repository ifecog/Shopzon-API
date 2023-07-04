import {
  // products list
  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL,
  // top rated products
  PRODUCT_TOP_RATED_REQUEST,
  PRODUCT_TOP_RATED_SUCCESS,
  PRODUCT_TOP_RATED_FAIL,
} from '../constants/productConstants'

export const productListReducer = (state = {products: []}, action) => {
  switch (action.type) {
    case PRODUCT_LIST_REQUEST:
      return {loading: true, products: []}

    case PRODUCT_LIST_SUCCESS:
      return {
        loading: false,
        products: action.payload.products,
        page: action.payload.page,
        pages: action.payload.pages,
      }

    case PRODUCT_LIST_FAIL:
      return {loading: false, error: action.payload}

    default:
      return state
  }
}

export const productTopRatedReducer = (state = {products: []}, action) => {
  switch (action.type) {
    case PRODUCT_TOP_RATED_REQUEST:
      return {loading: true, products: []}

    case PRODUCT_TOP_RATED_SUCCESS:
      return {
        loading: false,
        products: action.payload,
      }

    case PRODUCT_TOP_RATED_FAIL:
      return {loading: false, error: action.payload}

    default:
      return state
  }
}
