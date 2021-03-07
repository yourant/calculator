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
    id: number;
    name: string;
    category: string;
    description: string;
    featuredImage: string;
    images: [];
    location: string;
    date: Date;
    time: string;
}

