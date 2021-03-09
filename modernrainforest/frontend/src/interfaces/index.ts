export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileRegister {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
}

export interface IProductDetail {
    category_id: number;
    category: string;
    asin: string;
    plink: string;
    brand: string;
    price: [];
    rating: string;
    ranking: Date;
    mrevenue: string;
    msales: number;
    first_date: Date;
    dimensions: string;
    seller_num: number;
    seller_type: string;
}

