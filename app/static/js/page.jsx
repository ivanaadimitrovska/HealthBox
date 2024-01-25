// Page.js

import React from 'react';
import Navbar from './navbar';
import banner2 from '@/app/banners/image 4.png';
import Image from 'react-bootstrap/Image';

const Page = () => {
  return (
    <div className='container mt-3'>
      <Navbar />
      <div className='text-center'>
        <Image src={banner2} alt="Description of the image" fluid className='mt-4' />
        <p className='position-absolute top-50 start-50 translate-middle text-white' style={{ fontFamily: 'cursive', fontSize: '5rem', fontWeight: 'bold', marginLeft: '-20%' }}>Welcome to our Health Box</p>
      </div>
    </div>
  );
};

export default Page;
