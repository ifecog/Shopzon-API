import React, {useEffect} from 'react'
import {useSelector, useDispatch} from 'react-redux'
import {Link} from 'react-router-dom'
import {Carousel, Image} from 'react-bootstrap'
import Message from '../components/Message'
import Loader from '../components/Loader'
import {listTopRatedProducts} from '../actions/productActions'

function ProductCarousel() {
  const dispatch = useDispatch()

  const productTopRated = useSelector((state) => state.productTopRated)
  const {error, loading, products} = productTopRated

  useEffect(() => {
    dispatch(listTopRatedProducts())
  }, [dispatch])

  return loading ? (
    <Loader />
  ) : error ? (
    <Message variant='danger'>{error}</Message>
  ) : (
    <Carousel pause='hover' className='bg-dark'>
      {products.map((product) => (
        <Carousel.Item key={product._id}>
          <Link to={`/product/${product._id}`}>
            <Image src={product.image} alt={product.name} />
            <Carousel.Caption className='carousel.caption'>
              <h4>
                {product.name} (${product.price})
              </h4>
            </Carousel.Caption>
          </Link>
        </Carousel.Item>
      ))}
    </Carousel>
  )
}

export default ProductCarousel
