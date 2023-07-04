import React, {useState} from 'react'
import {Button, Form} from 'react-bootstrap'
import {useNavigate, useLocation} from 'react-router-dom'

function SearchBox() {
  const [keyword, setKeyword] = useState('')

  const navigate = useNavigate()
  const location = useLocation()

  const submitHandler = (e) => {
    e.preventDefault()
    if (keyword) {
      navigate(`/?keyword=${keyword}&page=1`)
    } else {
      navigate(navigate(location.pathname))
    }
  }

  return (
    <Form onSubmit={submitHandler} inline className='d-flex'>
      <Form.Control
        type='text'
        placeholder='search for products...'
        name='q'
        onChange={(e) => setKeyword(e.target.value)}
        className='mr-2 mx-1'
      ></Form.Control>

      <Button type='submit' variant='outline-success' className='p-2'>
        Search
      </Button>
    </Form>
  )
}

export default SearchBox
