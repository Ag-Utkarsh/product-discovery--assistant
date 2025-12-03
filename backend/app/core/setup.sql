-- 1. Enable Vector Extension
create extension if not exists vector;

-- 2. Products Table (The "Truth")
create table products (
  id uuid primary key default gen_random_uuid(),
  sku_id text unique not null,       --prevent duplicates
  title text not null,
  price integer not null,
  image_url text,
  source_url text,
  features jsonb,                    -- e.g. {"material": "wood", "dim": "6x6"}
  category text,                     -- e.g. "Bedroom"
  created_at timestamp with time zone default now()
);

-- 3. Embeddings Table (The "Search Engine")
create table product_embeddings (
  id uuid primary key default gen_random_uuid(),
  product_id uuid references products(id) on delete cascade,
  chunk_content text not null,       -- The text used for semantic search
  embedding vector(768)              -- Matching Gemini embedding size (768)
);

-- 4. Search Function (RPC)
create or replace function match_products (
  query_embedding vector(768),
  match_threshold float,
  match_count int
)
returns table (
  id uuid,
  product_id uuid,
  chunk_content text,
  similarity float
)
language plpgsql stable
as $$
begin
  return query
  select
    pe.id,
    pe.product_id,
    pe.chunk_content,
    1 - (pe.embedding <=> query_embedding) as similarity
  from product_embeddings pe
  where 1 - (pe.embedding <=> query_embedding) > match_threshold
  order by similarity desc
  limit match_count;
end;
$$;
