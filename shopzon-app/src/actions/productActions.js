import axios from 'axios'
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

export const listProducts =
  (keyword = '') =>
  async (dispatch) => {
    try {
      dispatch({
        type: PRODUCT_LIST_REQUEST,
      })

      const {data} = await axios.get(`/products/${keyword}`)

      dispatch({
        type: PRODUCT_LIST_SUCCESS,
        payload: data,
      })
    } catch (error) {
      dispatch({
        type: PRODUCT_LIST_FAIL,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      })
    }
  }

export const listTopRatedProducts = () => async (dispatch) => {
  try {
    dispatch({
      type: PRODUCT_TOP_RATED_REQUEST,
    })

    const {data} = await axios.get('/products/top_products')

    dispatch({
      type: PRODUCT_TOP_RATED_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: PRODUCT_TOP_RATED_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    })
  }
}
