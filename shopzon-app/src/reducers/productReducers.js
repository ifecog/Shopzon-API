import {
  // products list
  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL,
  // top rated products
  PRODUCT_TOP_RATED_REQUEST,
  PRODUCT_TOP_RATED_SUCCESS,
  PRODUCT_TOP_RATED_FAIL,
  // product details
  PRODUCT_DETAILS_REQUEST,
  PRODUCT_DETAILS_SUCCESS,
  PRODUCT_DETAILS_FAIL,
  // product reviews
  PRODUCT_CREATE_REVIEW_REQUEST,
  PRODUCT_CREATE_REVIEW_SUCCESS,
  PRODUCT_CREATE_REVIEW_FAIL,
  PRODUCT_CREATE_REVIEW_RESET,
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

export const productDetailsReducer = (
  state = {product: {reviews: []}},
  action
) => {
  switch (action.type) {
    case PRODUCT_DETAILS_REQUEST:
      return {loading: true, ...state}

    case PRODUCT_DETAILS_SUCCESS:
      return {
        loading: false,
        product: action.payload,
      }

    case PRODUCT_DETAILS_FAIL:
      return {loading: false, error: action.payload}

    default:
      return state
  }
}

export const productCreateReviewReducer = (state = {}, action) => {
  switch (action.type) {
    case PRODUCT_CREATE_REVIEW_REQUEST:
      return {loading: true}

    case PRODUCT_CREATE_REVIEW_SUCCESS:
      return {
        loading: false,
        success: true,
      }

    case PRODUCT_CREATE_REVIEW_FAIL:
      return {loading: false, error: action.payload}

    case PRODUCT_CREATE_REVIEW_RESET:
      return {}

    default:
      return state
  }
}
