#define conditional_negate(a,b,z) _mm512_mask_sub_epi8(a,_mm512_movepi8_mask(b),z,a)
static inline void nrLDPC_cnProc_BG2_R23_AVX512(int8_t* cnProcBuf, int8_t* cnProcBufRes, uint16_t Z) {
                uint32_t M;
                __m512i zmm0, min, sgn,zeros,ones,maxLLR;
                zeros  = _mm512_setzero_si512();
                maxLLR = _mm512_set1_epi8((char)127);
               ones = _mm512_set1_epi8((char)1);
//Process group with 3 BNs
//Process group with 4 BNs
 M = (1*Z + 63)>>6;
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[228+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[348+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[468+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[108+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[108+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[348+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[468+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[228+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[108+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[228+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[468+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[348+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[108+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[228+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[348+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[468+i] = conditional_negate(min, sgn,zeros);
            }
//Process group with 5 BNs
//Process group with 6 BNs
 M = (2*Z + 63)>>6;
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[876+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[894+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[912+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[930+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[948+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[858+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[858+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[894+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[912+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[930+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[948+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[876+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[858+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[876+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[912+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[930+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[948+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[894+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[858+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[876+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[894+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[930+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[948+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[912+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[858+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[876+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[894+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[912+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[948+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[930+i] = conditional_negate(min, sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[858+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[876+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[894+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[912+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[930+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[948+i] = conditional_negate(min, sgn,zeros);
            }
//Process group with 8 BNs
 M = (2*Z + 63)>>6;
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[978+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[990+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1002+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1014+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1026+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1038+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1050+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[966+i] = conditional_negate(min, sgn,zeros);
              }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[966+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[990+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1002+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1014+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1026+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1038+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1050+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[978+i] = conditional_negate(min, sgn,zeros);
              }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[966+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[978+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1002+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1014+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1026+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1038+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1050+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[990+i] = conditional_negate(min, sgn,zeros);
              }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[966+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[978+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[990+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1014+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1026+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1038+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1050+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1002+i] = conditional_negate(min, sgn,zeros);
              }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[966+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[978+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[990+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1002+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1026+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1038+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1050+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1014+i] = conditional_negate(min, sgn,zeros);
              }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[966+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[978+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[990+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1002+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1014+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1038+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1050+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1026+i] = conditional_negate(min, sgn,zeros);
              }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[966+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[978+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[990+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1002+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1014+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1026+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1050+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1038+i] = conditional_negate(min, sgn,zeros);
              }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[966+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[978+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[990+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1002+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1014+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1026+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1038+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1050+i] = conditional_negate(min, sgn,zeros);
              }
//Process group with 10 BNs
 M = (2*Z + 63)>>6;
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1062+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1074+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1086+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1098+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1110+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1122+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1134+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1146+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1170+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1158+i] = conditional_negate(min,sgn,zeros);
            }
            for (int i=0;i<M;i++) {
                zmm0 = ((__m512i*)cnProcBuf)[1062+i];
                sgn  = _mm512_xor_si512(ones, zmm0);
                min  = _mm512_abs_epi8(zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1074+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1086+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1098+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1110+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1122+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1134+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1146+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                zmm0 = ((__m512i*)cnProcBuf)[1158+i];
                min  = _mm512_min_epu8(min, _mm512_abs_epi8(zmm0));
                sgn  = _mm512_xor_si512(sgn, zmm0);
                min = _mm512_min_epu8(min, maxLLR);
                ((__m512i*)cnProcBufRes)[1170+i] = conditional_negate(min,sgn,zeros);
            }
}
