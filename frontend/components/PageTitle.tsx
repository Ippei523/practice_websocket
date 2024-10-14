import { Text } from "@chakra-ui/react";

export default function PageTitle({
  title,
}: Readonly<{
  title: string;
}>) {
  return (
    <>
      <Text
        fontSize={["2xl", "3xl"]}
        fontWeight="bold"
        mt={8}
        mb={4}
      >{title}</Text>
    </>
  );
}