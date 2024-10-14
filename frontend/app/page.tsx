import PageTitle from "@/components/PageTitle";
import { Box, ChakraProvider, Link } from "@chakra-ui/react";

export default function Home() {
  return (
    <ChakraProvider>
      <Box>
        <PageTitle title="Home" />
      </Box>
      {/* いい感じにデザインして欲しい */}
      <Box display={"flex"} flexDir={"column"}>
        {/* ページ遷移させたい */}
        <Link href="/user-info">ユーザー情報</Link>
        <Link href="/friend">友達</Link>
        <Link href="/chat">チャット</Link>
      </Box>
    </ChakraProvider>
  );
}
