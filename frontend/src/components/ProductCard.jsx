import React from 'react';
import { Link } from 'react-router-dom';

const ProductCard = ({ product }) => {
    return (
        <Link to={`/product/${product.id}`} className="group block relative">
            <div className="aspect-[5/6] w-full overflow-hidden bg-gray-100">
                <img
                    src={product.image_url}
                    alt={product.title}
                    className="h-full w-full object-cover object-center group-hover:scale-105 transition-transform duration-300"
                />
                <button className="absolute top-2 right-2 p-2 text-white hover:text-gray-200">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                    </svg>
                </button>
            </div>
            <div className="mt-4 flex justify-between items-start">
                <div>
                    <h3 className="text-base font-bold text-gray-900 uppercase tracking-wide">{product.title}</h3>
                    <p className="text-lg font-medium text-black">₹{product.price}</p>
                </div>
            </div>
        </Link>
    );
};

export default ProductCard;
