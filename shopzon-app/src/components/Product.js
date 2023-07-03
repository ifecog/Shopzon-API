import React from 'react'
import {Card} from 'react-bootstrap'
import Rating from './Rating'
import {Link} from 'react-router-dom'

function Product({product}) {
  return (
    <Card className='my-3 p-3 rounded'>
      <Link to={`/product/${product._id}`}>
        <Card.Img src={product.image} />
      </Link>

      <Card.Body>
        <Link
          to={`/product/${product._id}`}
          className='list-group-item-no-decoration'
        >
          <Card.Title as='div'>
            <strong>{product.name}</strong>
          </Card.Title>
        </Link>

        <Card.Title as='div'>
          <strong>Category:{product.category}</strong>
        </Card.Title>

        <Card.Title as='div'>
          <strong>Brand:{product.brand}</strong>
        </Card.Title>

        <Card.Text as='div'>
          <div className='my-3'>
            <Rating
              value={product.rating}
              text={
                <div
                  style={{whiteSpace: 'pre-wrap'}}
                >{`${product.num_of_reviews} reviews`}</div>
              }
              color={'#f8e825'}
            />
          </div>
        </Card.Text>

        <Card.Text as='h3'>${product.price}</Card.Text>
      </Card.Body>
    </Card>
  )
}

export default Product
