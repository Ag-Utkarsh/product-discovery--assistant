import React from 'react';

const ProductCardSkeleton = () => {
    return (
        <div className="animate-pulse">
            {/* Image skeleton */}
            <div className="aspect-[5/6] w-full bg-gray-200 rounded"></div>

            {/* Text skeleton */}
            <div className="mt-4 space-y-2">
                <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                <div className="h-5 bg-gray-200 rounded w-1/4"></div>
            </div>
        </div>
    );
};

export default ProductCardSkeleton;
