import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Container from '@mui/material/Container';
import { styled } from '@mui/material/styles';

// Styled components for custom styling
const ShowcaseCard = styled(Card)(({ theme }) => ({
  maxWidth: 300,
  width: '100%',
  transition: 'transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out',
  '&:hover': {
    transform: 'translateY(-4px)',
    boxShadow: theme.shadows[8],
  },
  backgroundColor: theme.palette.background.paper,
  borderRadius: theme.shape.borderRadius,
}));

const ShowcaseMedia = styled(CardMedia)(({ theme }) => ({
  height: 280,
  objectFit: 'contain',
  padding: theme.spacing(2),
  backgroundColor: theme.palette.background.default,
}));

const ShowcaseContent = styled(CardContent)(({ theme }) => ({
  padding: theme.spacing(2),
  '&:last-child': {
    paddingBottom: theme.spacing(2),
  },
}));

const ProductName = styled(Typography)(({ theme }) => ({
  fontWeight: 500,
  textAlign: 'center',
  color: theme.palette.text.primary,
}));

export default function ProductShowcase() {
  const products = [
    { 
      id: 1, 
      name: "Doudoune bleue Tommy Hilfiger", 
      image: "./src/marketing-page/components/imagesShowcase/1t.png"
    },
    { 
      id: 2, 
      name: "Baskets en cuir Tommy Hilfiger", 
      image: "./src/marketing-page/components/imagesShowcase/2t.png"
    },
    { 
      id: 3, 
      name: "Air Jordan 4 \"Fear\"", 
      image: "./src/marketing-page/components/imagesShowcase/3aj.png"
    },
  ];

  return (
    <Box id="Showcase" sx={{ py: 4 }}>
      <Typography
        component="p"
        variant="subtitle2"
        align="center"
        sx={{ color: 'text.secondary' }}
      >
        Nos produits mis en avant :
      </Typography>
    <Container maxWidth="lg">
      <Box
        sx={{
          display: 'grid',
          gridTemplateColumns: {
            xs: '1fr',
            sm: 'repeat(2, 1fr)',
            md: 'repeat(3, 1fr)',
          },
          gap: 3,
          py: 4,
        }}
      >
        {products.map((product) => (
          <ShowcaseCard key={product.id}>
            <img src={product.image} alt={product.name} style={{width: "100%", borderRadius: "10px"}} />
            <ShowcaseContent>
              <ProductName variant="h6" component="h3">
                {product.name}
              </ProductName>
            </ShowcaseContent>
          </ShowcaseCard>
        ))}
      </Box>
    </Container>
    </Box>
  );
}